package moves;
import ru.ifmo.se.pokemon.*;
public final class Facade extends PhysicalMove {
    public Facade() {
        super(Type.NORMAL, 70, 1.0);
    }
    @Override
    protected double calcBaseDamage(Pokemon att, Pokemon def) {
        Status st = att.getCondition();
        if (st.equals(Status.POISON) || st.equals(Status.PARALYZE) || st.equals(Status.BURN)) {
            return super.calcBaseDamage(att, def) * 2;
        }
        return super.calcBaseDamage(att, def);
    }
    @Override
    protected String describe() {
        return "uses Facade";
    }
}
