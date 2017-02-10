////////////////////////////////////////////////////////////////////////////////////
//
//  C212 Spring 16
//
//  Homework 6 Template
//  Due: Friday 3/11 11:59 pm
//  @Author  Earl Dean
//
// Modified By: James Gregory
// Last Modified: 3/23/16
//
///////////////////////////////////////////////////////////////////////////////////

import javax.swing.JFrame;
import javax.swing.JPanel;

import java.awt.Container;

/*
 * Main application for random rhape renerator app
 */
public class ShapeWindow extends JFrame {

    JPanel shapeDriver;

    public ShapeWindow() {
        super("Brick Break");
        shapeDriver = new ShapeDriver();   
        
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        Container surface = getContentPane();
        surface.add(shapeDriver);
        pack();
        setLocationRelativeTo(null);
        setAlwaysOnTop(true);
        setVisible(true);
        setAlwaysOnTop(false);
    }

    public static void main(String[] args) {
      new ShapeWindow();
    }
}
