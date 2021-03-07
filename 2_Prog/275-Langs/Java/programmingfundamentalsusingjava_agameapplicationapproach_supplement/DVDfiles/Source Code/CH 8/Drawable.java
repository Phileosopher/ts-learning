    import java.awt.*;

    public interface Drawable
    {
      boolean canDraw(int drawableWidth, int drawableHeight);
      void show(Graphics g);
    }
