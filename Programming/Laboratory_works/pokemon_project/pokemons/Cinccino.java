package pokemons;
import ru.ifmo.se.pokemon.*;
import moves.*;
public final class Cinccino extends Minccino {
    public Cinccino(String name, int level) {
        super(name, level);
        setType(Type.NORMAL);
        setStats(75, 95, 60, 65, 60, 115);
        addMove(new Thunderbolt());
        addMove(new Facade());
        addMove(new Rest());
        addMove(new FocusBlast());
    }
}
