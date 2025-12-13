package pokemons;
import ru.ifmo.se.pokemon.*;
import moves.*;
public final class Raikou extends Pokemon {
    public Raikou(String name, int level) {
        super(name, level);
        setType(Type.ELECTRIC);
        setStats(90, 85, 75, 115, 100, 115);
        addMove(new Swagger());
        addMove(new Thunder());
        addMove(new Bulldoze());
        addMove(new Thunderbolt());
    }
}
