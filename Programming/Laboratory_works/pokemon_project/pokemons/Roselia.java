package pokemons;
import ru.ifmo.se.pokemon.*;
import moves.*;
public class Roselia extends Budew {
    public Roselia(String name, int level) {
        super(name, level);
        setType(Type.GRASS, Type.POISON);
        setStats(50, 60, 45, 100, 80, 65);
        addMove(new Rest());
        addMove(new Confide());
        addMove(new StunSpore());
    }
}
