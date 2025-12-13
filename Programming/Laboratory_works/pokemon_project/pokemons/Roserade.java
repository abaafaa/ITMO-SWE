package pokemons;
import ru.ifmo.se.pokemon.*;
import moves.*;
public final class Roserade extends Roselia {
    public Roserade(String name, int level) {
        super(name, level);
        setType(Type.GRASS, Type.POISON);
        setStats(60, 70, 65, 125, 105, 90);
        addMove(new Rest());
        addMove(new Confide());
        addMove(new StunSpore());
        addMove(new EnergyBall());
    }
}
