package pokemons;
import ru.ifmo.se.pokemon.*;
import moves.*;
public class Minccino extends Pokemon {
    public Minccino(String name, int level) {
        super(name, level);
        setType(Type.NORMAL);
        setStats(55, 50, 40, 40, 40, 75);
        addMove(new Thunderbolt());
        addMove(new Facade());
        addMove(new Rest());
        addMove(new Confide());
    }
}
