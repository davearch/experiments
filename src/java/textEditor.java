import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.io.*;


@SuppressWarnings("serial")
public class textEditor extends JFrame implements ActionListener, WindowListener {
	
	private JTextArea jta=new JTextArea();
	private File fnameContainer;
	
	public textEditor(){
		Font fnt=new Font("Times New Roman",Font.PLAIN,15);
		Container con=getContentPane();
		JMenuBar jmb=new JMenuBar();
		JMenu jmfile = new JMenu("File");
		JMenu jmedit = new JMenu("Edit");
		JMenu jmhelp = new JMenu("Help");
		
		con.setLayout(new BorderLayout());
		JScrollPane sbrText = new JScrollPane(jta);
		sbrText.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
		sbrText.setVisible(true);
		
		jta.setFont(fnt);
		jta.setLineWrap(true);
		jta.setWrapStyleWord(true);
		con.add(sbrText);

		createMenuItem(jmfile,"New");
		createMenuItem(jmfile,"Open");
		createMenuItem(jmfile,"Save");
		jmfile.addSeparator();
		createMenuItem(jmfile,"Exit");
		
		createMenuItem(jmedit,"Cut");
		createMenuItem(jmedit,"Copy");
		createMenuItem(jmedit,"Paste");
		createMenuItem(jmhelp,"About textEditor");
		
		jmb.add(jmfile);
		jmb.add(jmedit);
		jmb.add(jmhelp);
		setJMenuBar(jmb);
		setIconImage(Toolkit.getDefaultToolkit().getImage("textEditor.gif"));
		addWindowListener(this);
		setSize(500,500);
		setTitle("Untitled.txt - textEditor");		
		setVisible(true);
	
	}

	public void createMenuItem(JMenu jm, String txt){
		JMenuItem jmi=new JMenuItem(txt);
		jmi.addActionListener(this);
		jm.add(jmi);
	}
	
	public void actionPerformed(ActionEvent e){	
		JFileChooser jfc=new JFileChooser();
		int ret;
		switch (e.getActionCommand()){
			case "New": 			this.setTitle("Untitled.txt - textEditor");
									jta.setText("");
									fnameContainer = null;
									break;
			case "Open":			ret = jfc.showDialog(null, "Open");
									if (ret == JFileChooser.APPROVE_OPTION){
										try {
											File fyl = jfc.getSelectedFile();
											OpenFile(fyl.getAbsolutePath());
											this.setTitle(fyl.getName() + " - textEditor");
											fnameContainer = fyl;
										} catch(IOException ers){}
									}
									break;
			case "Save":			if (fnameContainer != null) {
										jfc.setCurrentDirectory(fnameContainer);
										jfc.setSelectedFile(fnameContainer);
									} else {
										jfc.setSelectedFile(new File("Untitled.txt"));
									}
									ret = jfc.showSaveDialog(null);
									if (ret == JFileChooser.APPROVE_OPTION) {
										try {
											File fyl=jfc.getSelectedFile();
											SaveFile(fyl.getAbsolutePath());
											this.setTitle(fyl.getName()+ " - textEditor");
											fnameContainer=fyl;
										} catch(Exception ers2){}
									}
									break;
			case "Exit":			Exiting();
									break;
			case "Copy":			jta.copy();
									break;
			case "Paste":			jta.paste();
									break;
			case "About textEditor":	JOptionPane.showMessageDialog(this,"David Archuleta (http://www.azslr.com)","textEditor",JOptionPane.INFORMATION_MESSAGE);
									break;
			case "Cut":				jta.cut();
									break;
			default:				// do nothing
									break;
		}
	}
	
	public void OpenFile(String fname) throws IOException {	
		BufferedReader d=new BufferedReader(new InputStreamReader(new FileInputStream(fname)));
		String l;
		jta.setText("");
	
		setCursor(new Cursor(Cursor.WAIT_CURSOR));
			
		while((l=d.readLine())!= null) {
			jta.setText(jta.getText()+l+"\r\n");
		}
		
		setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
		d.close();
	}
	
	public void SaveFile(String fname) throws IOException {
		setCursor(new Cursor(Cursor.WAIT_CURSOR));
		DataOutputStream o=new DataOutputStream(new FileOutputStream(fname));
		o.writeBytes(jta.getText());
		o.close();		
		setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
	}
	
	public void windowDeactivated(WindowEvent e){}
	public void windowActivated(WindowEvent e){}
	public void windowDeiconified(WindowEvent e){}
	public void windowIconified(WindowEvent e){}
	public void windowClosed(WindowEvent e){}
	
	public void windowClosing(WindowEvent e) {
		Exiting();
	}
	
	public void windowOpened(WindowEvent e){}
	
	public void Exiting() {
		System.exit(0);
	}
	
	public static void main (String[] args) {	
		new textEditor();
	}	
}
