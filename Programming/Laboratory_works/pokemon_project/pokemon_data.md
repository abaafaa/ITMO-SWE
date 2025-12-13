# Информация о Покемонах и Атаках

## Покемоны и их характеристики

| Покемон | Тип(ы) | HP | Attack | Defense | Sp. Atk | Sp. Def | Speed | Цепочка эволюции |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Raikou** | Electric | 90 | 85 | 75 | 115 | 100 | 115 | Не эволюционирует |
| **Budew** | Grass, Poison | 40 | 30 | 35 | 50 | 70 | 55 | Budew -> Roselia -> Roserade |
| **Roselia** | Grass, Poison | 50 | 60 | 45 | 100 | 80 | 65 | Budew -> Roselia -> Roserade |
| **Roserade** | Grass, Poison | 60 | 70 | 65 | 125 | 105 | 90 | Budew -> Roselia -> Roserade |
| **Minccino** | Normal | 55 | 50 | 40 | 40 | 40 | 75 | Minccino -> Cinccino |
| **Cinccino** | Normal | 75 | 95 | 60 | 65 | 60 | 115 | Minccino -> Cinccino |

## Атаки и их характеристики

| Атака | Класс | Тип | Power | Accuracy | Эффект |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Swagger** | StatusMove | Normal | - | 85 | Увеличивает Attack цели на 2 ступени и сбивает с толку (Confuse). |
| **Thunder** | SpecialMove | Electric | 110 | 70 | 30% шанс парализовать цель. Точность 100% в дожде. |
| **Bulldoze** | PhysicalMove | Ground | 60 | 100 | Снижает Speed цели на 1 ступень. |
| **Thunderbolt** | SpecialMove | Electric | 90 | 100 | 10% шанс парализовать цель. |
| **Facade** | PhysicalMove | Normal | 70 | 100 | Удваивает силу (до 140), если пользователь отравлен, парализован или обожжен. |
| **Rest** | StatusMove | Psychic | - | - | Пользователь засыпает на 2 хода, полностью восстанавливает HP и снимает все статусные эффекты. |
| **Focus Blast** | SpecialMove | Fighting | 120 | 70 | 10% шанс снизить Sp. Def цели на 1 ступень. |
| **Confide** | StatusMove | Normal | - | - | Снижает Sp. Atk цели на 1 ступень. Не промахивается. |
| **Stun Spore** | StatusMove | Grass | - | 75 | Парализует цель. |
| **Energy Ball** | SpecialMove | Grass | 90 | 100 | 10% шанс снизить Sp. Def цели на 1 ступень. |

## Распределение атак по Покемонам

| Покемон | Атаки |
| :--- | :--- |
| **Raikou** | Swagger, Thunder, Bulldoze, Thunderbolt |
| **Minccino** | Thunderbolt, Facade, Rest, Confide |
| **Cinccino** | Thunderbolt, Facade, Rest, Focus Blast |
| **Budew** | Rest, Confide |
| **Roselia** | Rest, Confide, Stun Spore |
| **Roserade** | Rest, Confide, Stun Spore, Energy Ball |

## Минимальный уровень
Минимальный уровень покемона будет установлен на 1, так как в задании не указано, что атаки должны быть изучены на определенном уровне, а только то, что уровень должен быть "минимально необходимым для всех реализованных атак". В контексте этого задания, это означает, что все атаки будут доступны с самого начала.

## Команды для симуляции
**Команда 1:** Raikou, Cinccino, Roserade
**Команда 2:** Minccino, Roselia, Budew

## Структура проекта
- `src/`
    - `ru/ifmo/pokemons/`
        - `Raikou.java`
        - `Minccino.java`
        - `Cinccino.java`
        - `Budew.java`
        - `Roselia.java`
        - `Roserade.java`
    - `ru/ifmo/moves/`
        - `Swagger.java`
        - `Thunder.java`
        - `Bulldoze.java`
        - `Thunderbolt.java`
        - `Facade.java`
        - `Rest.java`
        - `FocusBlast.java`
        - `Confide.java`
        - `StunSpore.java`
        - `EnergyBall.java`
    - `BattleSimulation.java` (Главный класс)
- `Pokemon.jar` (предоставленный файл)
- `compile.sh` (скрипт для компиляции)
- `run.sh` (скрипт для запуска)
