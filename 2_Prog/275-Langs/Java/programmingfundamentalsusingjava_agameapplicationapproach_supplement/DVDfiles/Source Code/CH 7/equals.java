      public boolean equals(ParentSnowman ps) //a deep comparison
      {
        if(x == ps.getX() && y == ps.getY() &&
           name.equals(ps.getName())) 
        {  
          return true; //same location and family name
        }
        else
        {
          return false; //different location and/or family name 
        }     
      }
