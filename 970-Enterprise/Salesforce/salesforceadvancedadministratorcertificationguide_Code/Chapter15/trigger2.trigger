trigger OpportunityTrigger on Opportunity (before insert, before update, before delete,
                                           after insert, after update, after delete, after undelete) {
     if(Trigger.isBefore){
         
         if(Trigger.isInsert || Trigger.isUpdate){
             //before logic goes here...
         }

         if(Trigger.isUpdate){
             //before logic goes here...
         }
     }else if(Trigger.isAfter){
         if(Trigger.isUpdate || Trigger.isInsert){
         	//after logic goes here...
         }
     }
 }