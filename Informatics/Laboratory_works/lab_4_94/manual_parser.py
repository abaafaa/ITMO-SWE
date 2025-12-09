import re

def _parse_value(val_str):
    val_str = val_str.strip()
    if val_str.lower() == "true":
        return True
    elif val_str.lower() == "false":
        return False
    elif val_str.startswith("[") and val_str.endswith("]"):
        items = [item.strip() for item in val_str[1:-1].split(",")]
        return [_parse_value(item) for item in items if item]
    elif val_str.isdigit():
        return int(val_str)
    elif re.match(r"^\d+\.\d+$", val_str):
        return float(val_str)
    else:
        if val_str.startswith('"') and val_str.endswith('"'):
            val_str = val_str[1:-1]
        return val_str

def _parse_block(lines, start_idx):
    result = {}
    i = start_idx
    block_list = []

    while i < len(lines):
        line = lines[i].strip()
        i += 1

        if not line or line.startswith("#"):
            continue

        if line == "}":
            break

        if line.endswith("{"):
            parts = line[:-1].strip().split()
            block_name = parts[0]
            block_key = parts[1].strip('"') if len(parts) > 1 else None

            block_content, i = _parse_block(lines, i)

            key = block_name
            if key not in result:
                result[key] = []
            
            if block_key:
                block_content['key'] = block_key
            
            result[key].append(block_content)

        elif "=" in line:
            key, val_str = line.split("=", 1)
            key = key.strip()
            val_str = val_str.strip().rstrip(",").strip()
            result[key] = _parse_value(val_str)

    return result, i

def parse_hcl(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    first_line = lines[0].strip()
    if not first_line.endswith("{"):
        raise ValueError("Invalid HCL format: expected top-level block.")

    top_key = first_line.split("{")[0].strip()

    data, _ = _parse_block(lines, 1)

    return {top_key: data.get("day", [])}



def _format_yaml_value(value, indent):
    if isinstance(value, str):
        return f'"{value}"'
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, list):
        if not value:
            return "[]"
        
        if all(not isinstance(item, (dict, list)) for item in value):
            return f"[{', '.join([_format_yaml_value(item, 0) for item in value])}]"
        else:
            yaml_str = ""
            for item in value:
                yaml_str += f"\n{'  ' * indent}- "
                if isinstance(item, dict):
                    yaml_str += _to_yaml_string(item, indent + 1, is_list_item=True)
                else:
                    yaml_str += _format_yaml_value(item, 0)
            return yaml_str.lstrip('\n')
    else:
        return str(value)

def _to_yaml_string(data, indent=0, is_list_item=False):
    yaml_lines = []
    indent_str = '  ' * indent
    
    for key, value in data.items():
        if key == 'key':
            continue
            
        line_prefix = f"{indent_str}{key}: "
        
        if isinstance(value, dict):
            yaml_lines.append(f"{line_prefix}")
            yaml_lines.append(_to_yaml_string(value, indent + 1))
        elif isinstance(value, list) and value and isinstance(value[0], dict):
            yaml_lines.append(f"{line_prefix}")
            for item in value:
                yaml_lines.append(f"{'  ' * (indent + 1)}- {_to_yaml_string(item, indent + 2, is_list_item=True).lstrip()}")
        elif isinstance(value, list):
            yaml_lines.append(f"{line_prefix}{_format_yaml_value(value, indent)}")
        else:
            yaml_lines.append(f"{line_prefix}{_format_yaml_value(value, indent)}")

    return "\n".join(yaml_lines)

def to_yaml(data, filename):
    yaml_content = _to_yaml_string(data)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(yaml_content)



def _escape_xml(text):
    if text is None:
        return ""
    text = str(text)
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace('"', "&quot;")
    text = text.replace("'", "&apos;")
    return text

def _sanitize_tag_name(name):
    name = str(name)
    sanitized = re.sub(r'[^\w-]', '_', name)
    if sanitized and sanitized[0].isdigit():
        sanitized = f"_{sanitized}"
    return sanitized if sanitized else "item"

def _dict_to_xml(data, indent=0):
    spaces = "  " * indent
    result = []

    for key, value in data.items():
        if key == 'key':
            continue
            
        tag = _sanitize_tag_name(key)

        if isinstance(value, dict):
            result.append(f"{spaces}<{tag}>")
            result.append(_dict_to_xml(value, indent + 1))
            result.append(f"{spaces}</{tag}>")
        elif isinstance(value, list):
            result.append(f"{spaces}<{tag}>")
            for item in value:
                if isinstance(item, dict):
                    item_tag = _sanitize_tag_name(item.get('key', 'item'))
                    result.append(f"{spaces}  <{item_tag}>")
                    result.append(_dict_to_xml(item, indent + 2))
                    result.append(f"{spaces}  </{item_tag}>")
                else:
                    escaped = _escape_xml(item)
                    result.append(f"{spaces}  <item>{escaped}</item>")
            result.append(f"{spaces}</{tag}>")
        else:
            escaped = _escape_xml(value)
            result.append(f"{spaces}<{tag}>{escaped}</{tag}>")

    return "\n".join(result)

def to_xml(data, filename):
    xml_content = _dict_to_xml(data, 1)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<config>\n{xml_content}\n</config>")


def to_bin(data, filename):
    data_str = str(data)
    with open(filename, "wb") as f:
        f.write(data_str.encode("utf-8"))

def from_bin(filename):
    with open(filename, "rb") as f:
        data_str = f.read().decode("utf-8")
    return eval(data_str)
