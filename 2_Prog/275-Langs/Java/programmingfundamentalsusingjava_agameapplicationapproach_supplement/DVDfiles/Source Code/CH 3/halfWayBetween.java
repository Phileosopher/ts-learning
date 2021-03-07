   public static SnowmanV6 halfWayBetween(SnowmanV6 sm1,SnowmanV6 sm2)
   {
     int x, y;
     SnowmanV6 aSnowman = new SnowmanV6();

     x = (sm1.getX() + sm2.getX()) / 2;    
     y = (sm1.getY() + sm2.getY()) / 2;    
     aSnowman.setX(x);
     aSnowman.setY(y);

    return aSnowman;
  }
