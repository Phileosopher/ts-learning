  import java.util.TreeMap;
  import javax.swing.*;

  public class TreeMapApp 
  {
    public static void main(String[] args) 
    {
      TreeMap<String, Patient>patientInfo = new TreeMap<String, Patient>();
      String lastName;
      Patient p1 = new Patient("Tom Jones", "2/3/1989", "643 976-4545");
      Patient p2 = new Patient("Amy Adams", "8/5/1991", "643 531-2283");
      Patient p3 = new Patient("Norm Baum", "5/9/1945", "541 386-2371");
      Patient p4 = new Patient("Ray Rondo", "2/6/1998", "643 736-2949");
      Patient aPatient;

      //Save the key and value pairs in the collection
      patientInfo.put("Jones", p1);
      patientInfo.put("Adams", p2);
      patientInfo.put("Baum", p3);
      patientInfo.put("Rondo", p4);

      //Fetch and output a patient's value (object)
      lastName = JOptionPane.showInputDialog("Enter a patient's last " +
                                             "name \nClick Cancel " +
                                             "to output all patients");
      while(lastName != null) //not a Cancel click
      {
        aPatient = patientInfo.get(lastName);
        if(aPatient == null) //key is not in collection
        {
          JOptionPane.showMessageDialog(null, "That person is not in" +
                                              "our data base");
        }
        else //output the value
        {
          JOptionPane.showMessageDialog(null, aPatient);
        }
        lastName = JOptionPane.showInputDialog("Enter a patient's last " +
                                               "name \nClick Cancel " +
                                               "to output all patients");
      }

      //Output all patients
      for (String key: patientInfo.keySet())//all keys in the collection 
      {
        aPatient = patientInfo.get(key);  
        System.out.println(aPatient);  
      }
    }
  }
