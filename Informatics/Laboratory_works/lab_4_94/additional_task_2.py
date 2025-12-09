import hcl2
import yaml
import json

INPUT_FILE = "config/input.hcl"
OUTPUT_FILE = "config/output_task2.yaml"

def run_additional_task_2():
    print(f"Парсинг {INPUT_FILE} с помощью библиотеки hcl...")
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        config_data = hcl2.load(f)
    
    print(f"Конвертация в YAML и запись в {OUTPUT_FILE} с помощью библиотеки yaml...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(config_data, f, allow_unicode=True, default_flow_style=False)
        
    print("Задание выполнено.")

if __name__ == "__main__":
    run_additional_task_2()
