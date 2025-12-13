package moves;
import ru.ifmo.se.pokemon.*;
public final class Rest extends StatusMove {
    public Rest() {
        super(Type.PSYCHIC, 0, 1.0);
    }
    @Override
    protected void applySelfEffects(Pokemon p) {
        p.setMod(Stat.HP, (int) (p.getStat(Stat.HP) - p.getHP()));
        p.restore();
        Effect e = new Effect().condition(Status.SLEEP).turns(2);
        p.addEffect(e);
    }
    @Override
    protected String describe() {
        return "uses Rest";
    }
}
