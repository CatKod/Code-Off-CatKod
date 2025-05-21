import java.awt.*;

public class MouseEventDemo extends Frame {  
    private TextField tfMouseX; // to display mouse-click-x  
    private TextField tfMouseY; // to display mouse-click-y  

    // Setup the UI components and event handlers  
    public MouseEventDemo() {     
        setLayout(new FlowLayout());
        add(new Label("X-Click: "));
        tfMouseX = new TextField(10); // 10 columns
        tfMouseX.setEditable(false);
        add(tfMouseX);

        add(new Label("Y-Click: "));
        tfMouseY = new TextField(10);
        tfMouseY.setEditable(false);
        add(tfMouseY);    
 
        addMouseListener(new MyMouseListener(tfMouseX, tfMouseY));

        setTitle("MouseEvent Demo");
        setSize(350, 100);
        setVisible(true);
    }  

    public static void main(String[] args) {     
        new MouseEventDemo();  // Let the constructor do the job  
    }
}
