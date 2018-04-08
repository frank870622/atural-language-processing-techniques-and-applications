import java.net.Socket;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.FileInputStream;
 
public class CKIPWS {
	
    private String address;// 連線的ip
    private int port;// 連線的port
    private Socket client;
 
    public CKIPWS(String addr, int port) {
        this.address = addr;
        this.port = port;
    }
    
    public ArrayList<Tuple<String, String>> seg(String Sent){
    	
    	ArrayList<Tuple<String, String>> WSResult = new ArrayList<Tuple<String, String>>();
    	
        try {
        	
        	client = new Socket(this.address, this.port);
        	
            //Send Sentence
        	BufferedOutputStream out = new BufferedOutputStream(client.getOutputStream());
            String outmsg = "seg@@" + Sent;
            out.write(outmsg.getBytes(Charset.forName("UTF-8")));
            out.flush();
            //out.close();
            
            //Receive Result
            BufferedInputStream in = new BufferedInputStream(client.getInputStream());
            byte[] b = new byte[1024];
            String msg = "";
            while (in.read(b) > 0)// <=0的話就是結束了
            	msg += new String(b, Charset.forName("UTF-8"));
            
            out.close();
            in.close();
            client.close();
            
            String[] terms = msg.replace("\n", "").replace("\0", "").split("　");
            for(int i = 0; i < terms.length; i++){
            	String [] temp = terms[i].substring(0, terms[i].length() - 1).split("\\(");
            	Tuple<String, String> pair = new Tuple<String, String>(temp[0], temp[1]); 
            	WSResult.add(pair);
            }
            
        } catch (java.io.IOException e) {
            System.out.println("Socket連線有問題 !");
            System.out.println("IOException :" + e.toString());
        }
        
        return WSResult;
    }
    
    public void destroy(){
    	client = null;
    }
    
    public class Tuple<X, Y> { 
  	  public final X word; 
  	  public final Y pos; 
  	  public Tuple(X x, Y y) { 
  	    this.word = x; 
  	    this.pos = y; 
  	  }
    }
    
    public static void main(String[] args) {
    	Scanner scanner;
    	try {
    		scanner = new Scanner(new FileInputStream("good.txt"));
    		Set<String> setGood = new HashSet<>();
    		while (scanner.hasNextLine()) {
				setGood.add(scanner.nextLine());
			}
    		scanner = new Scanner(new FileInputStream("bad.txt"));
    		Set<String> setBad = new HashSet<>();
    		while (scanner.hasNextLine()) {
				setBad.add(scanner.nextLine());
			}
    		
    		// TODO Auto-generated method stub
    		CKIPWS WS = new CKIPWS("140.116.245.151", 2001);
    		scanner = new Scanner(System.in);
    		String string = scanner.nextLine();
    		ArrayList<CKIPWS.Tuple<String, String>> x = WS.seg(string);
    		System.out.println("CKIP斷詞結果 CKIP Word Segmentation Result");
    		for(int i = 0; i < x.size(); i++){
    			System.out.print(x.get(i).word + " (" + x.get(i).pos + ") ");
    		}
    		System.out.println();
    		
    		//Person Name List
    		System.out.println("人名識別 Person Name List");
    		for(int i = 0; i < x.size(); i++){
    			if(x.get(i).pos == "Nb")
    				System.out.print(x.get(i).word + " ");
    		}
    		System.out.println();
    		
    		//Event List
    		System.out.println("事件識別  Event List");
    		
    		//Time List
    		System.out.println("時間識別 Time List");
    		for(int i = 0; i < x.size(); i++){
    			if(x.get(i).pos == "Nd")
    				System.out.print(x.get(i).word + " ");
    		}	
    		System.out.println();
    		
    		//Location List
    		System.out.println("地名識別 Location List");
    		for(int i = 0; i < x.size(); i++){
    			if(x.get(i).pos == "Nc")
    				System.out.print(x.get(i).word + " ");
    		}	
    		System.out.println();
    		
    		//Object List
    		System.out.println("物件識別 Object List");
    		for(int i = 0; i < x.size(); i++){
    			if(x.get(i).pos == "Na")
    				System.out.print(x.get(i).word + " ");
    		}	
    		System.out.println();
    		
    		//Emotion List
    		System.out.println("情緒識別 Emotion List");
    			//Positive emotion
    		System.out.println("Positive emotion");
    		for(int i = 0; i < x.size(); i++){
    			if(setGood.contains(x.get(i).word))
    				System.out.print(x.get(i).word + " ");
    		}	
    		System.out.println();
    			//Negative emotion
    		System.out.println("Negative emotion");
    		for(int i = 0; i < x.size(); i++){
    			if(setBad.contains(x.get(i).word))
    				System.out.print(x.get(i).word + " ");
    		}	
    		System.out.println();
		} catch (Exception e) {
			// TODO: handle exception
			System.out.println("nononono");
		}
		
	}
    
}

