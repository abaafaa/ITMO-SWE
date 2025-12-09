from manual_parser import parse_hcl, to_bin

INPUT_FILE = "config/input.hcl"
OUTPUT_FILE = "config/output_mandatory.bin"

def run_mandatory_task():
    print(f"Парсинг {INPUT_FILE} вручную...")
    config_data = parse_hcl(INPUT_FILE)
    
    print(f"Конвертация в бинарный объект и запись в {OUTPUT_FILE}...")
    to_bin(config_data, OUTPUT_FILE)
    print("Задание выполнено.")

if __name__ == "__main__":
    run_mandatory_task()
