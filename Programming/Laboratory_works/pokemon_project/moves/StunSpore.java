package moves;
import ru.ifmo.se.pokemon.*;
public final class StunSpore extends StatusMove {
    public StunSpore() {
        super(Type.GRASS, 0, 0.75);
    }
    @Override
    protected void applyOppEffects(Pokemon p) {
        Effect.paralyze(p);
    }
    @Override
    protected String describe() {
        return "uses Stun Spore";
    }
}
