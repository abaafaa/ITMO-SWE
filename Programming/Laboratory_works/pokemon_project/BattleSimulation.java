import ru.ifmo.se.pokemon.*;
import pokemons.*;
import moves.*;

public class BattleSimulation {
    public static void main(String[] args) {
        Battle b = new Battle();
        Pokemon raikou = new Raikou("Райкоу", 50);
        Pokemon minccino = new Minccino("Минcино", 15);
        Pokemon cinccino = new Cinccino("Cинcино", 40);
        Pokemon budew = new Budew("Будью", 10);
        Pokemon roselia = new Roselia("Розелия", 25);
        Pokemon roserade = new Roserade("Роузрейд", 40);
        b.addAlly(raikou);
        b.addAlly(cinccino);
        b.addAlly(roserade);
        b.addFoe(minccino);
        b.addFoe(roselia);
        b.addFoe(budew);
        b.go();
    }
}
