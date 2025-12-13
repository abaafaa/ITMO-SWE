#!/bin/bash
if [ ! -f Pokemon.jar ]; then
    echo "Ошибка: файл Pokemon.jar не найден. Пожалуйста, убедитесь, что он находится в /home/ubuntu/pokemon_project/"
    exit 1
fi

javac -cp .:Pokemon.jar -d . src/pokemons/*.java src/moves/*.java BattleSimulation.java

if [ $? -eq 0 ]; then
    echo "Компиляция успешно завершена."
else
    echo "Ошибка компиляции."
fi
