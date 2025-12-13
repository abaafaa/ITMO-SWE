package moves;
import ru.ifmo.se.pokemon.*;
public final class Swagger extends StatusMove {
    public Swagger() {
        super(Type.NORMAL, 0, 0.85);
    }
    @Override
    protected void applyOppEffects(Pokemon p) {
        p.setMod(Stat.ATTACK, 2);
        Effect.confuse(p);
    }
    @Override
    protected String describe() {
        return "uses Swagger";
    }
}
