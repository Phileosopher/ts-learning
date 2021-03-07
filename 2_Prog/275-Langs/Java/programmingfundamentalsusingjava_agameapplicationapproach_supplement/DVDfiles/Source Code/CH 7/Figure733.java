   enum Team {Yankees, Braves, Giants}
   
   Team myTeam = Team.Yankees;
   switch (myTeam)
   {
     case Yankees: // no type name qualifier used here
     System.out.println(myTeam + " " + Team.Yankees);
   }
