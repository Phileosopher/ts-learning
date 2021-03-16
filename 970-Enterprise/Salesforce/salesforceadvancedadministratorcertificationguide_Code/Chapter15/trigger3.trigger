trigger OpportunityTrigger on Opportunity (before insert, before update, before delete,
                                           after insert, after update, after delete, after undelete) {
     
     //current record (supposing only one opportunity can be saved at once)
     Opportunity currentOpp = Trigger.new[0];

     //treating before and after events separately
     if(Trigger.isBefore){
         
         //following logic 0runs in before insert and update
         if(Trigger.isInsert || Trigger.isUpdate){
             
             //error if opportunity has a negative amount
             if(currentOpp.Amount <= 0){
              //the addError() method is used to break the save process 
              //and is shown to the current user on the page layout 
              currentOpp.addError('Invalid negative amount on opportunity.');
             }

         }

         //folowing login runs only for before update
         if(Trigger.isUpdate){
             
             //gets the old values for an opportunity
             Opportunity oldOpp = Trigger.old[0];

             //error if opportunity amount is discounted of more than 50%
             Double newAmount = currentOpp.Amount;
             Double oldAmount = oldOpp.Amount;

             if(newAmount > 0 && oldAmount > 0 && newAmount < (oldAmount * 0.5) ){
              currentOpp.addError('Discount policies forbit discounts higher than 50%. Please review the deal. '+newAmount+' vs '+oldAmount);
             }

         }
     }else if(Trigger.isAfter){
         if(Trigger.isUpdate || Trigger.isInsert){
         	//after logic goes here...
         }
     }
 }