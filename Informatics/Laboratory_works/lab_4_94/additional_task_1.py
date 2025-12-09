from manual_parser import from_bin, to_yaml

INPUT_FILE = "config/output_mandatory.bin"
OUTPUT_FILE = "config/output_task1.yaml"

def run_additional_task_1():
    print(f"Парсинг бинарного объекта {INPUT_FILE} вручную...")
    config_data = from_bin(INPUT_FILE)
    
    print(f"Конвертация в YAML и запись в {OUTPUT_FILE} вручную...")
    to_yaml(config_data, OUTPUT_FILE)
    print("Задание выполнено.")

if __name__ == "__main__":
    run_additional_task_1()
