import timeit
import hcl2
from manual_parser import parse_hcl, to_yaml

INPUT_FILE = "config/input.hcl"
OUTPUT_FILE_MANUAL = "config/output_manual_temp.yaml"
OUTPUT_FILE_AUTO = "config/output_auto_temp.yaml"
ITERATIONS = 100

def manual_conversion():
    config_data = parse_hcl(INPUT_FILE)
    to_yaml(config_data, OUTPUT_FILE_MANUAL)

def auto_conversion():
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        config_data = hcl2.load(f)
    import yaml
    with open(OUTPUT_FILE_AUTO, 'w', encoding='utf-8') as f:
        yaml.dump(config_data, f, allow_unicode=True, default_flow_style=False)

def run_additional_task_4():
    print(f"Сравнение времени выполнения ({ITERATIONS} итераций):")
    
    print("1. Ручной парсинг HCL + Ручная сериализация в YAML...")
    time_manual = timeit.timeit(manual_conversion, number=ITERATIONS)
    print(f"   Общее время (ручной): {time_manual:.4f} сек")

    print("2. Библиотечный парсинг HCL + Библиотечная сериализация в YAML...")
    time_auto = timeit.timeit(auto_conversion, number=ITERATIONS)
    print(f"   Общее время (библиотечный): {time_auto:.4f} сек")
    
    print("\nРезультаты сравнения:")
    if time_manual < time_auto:
        print(f"Ручной метод быстрее на: {time_auto - time_manual:.4f} сек")
    else:
        print(f"Библиотечный метод быстрее на: {time_manual - time_auto:.4f} сек")
        
    import os
    os.remove(OUTPUT_FILE_MANUAL)
    os.remove(OUTPUT_FILE_AUTO)

if __name__ == "__main__":
    run_additional_task_4()
