import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.TextField;

public class MyMouseListener implements MouseListener {
    private TextField tfMouseX;
    private TextField tfMouseY;

    public MyMouseListener(TextField tfMouseX, TextField tfMouseY) {
        this.tfMouseX = tfMouseX;
        this.tfMouseY = tfMouseY;
    }

    @Override
    public void mousePressed(MouseEvent e) { }

    @Override
    public void mouseReleased(MouseEvent e) { }

    @Override
    public void mouseClicked(MouseEvent e) {
        tfMouseX.setText(e.getX() + "");
        tfMouseY.setText(e.getY() + "");
    }

    @Override
    public void mouseEntered(MouseEvent e) { }

    @Override
    public void mouseExited(MouseEvent e) {
        tfMouseX.setText("");
        tfMouseY.setText("");
    }
}
