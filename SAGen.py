import sys
import numpy as np
import random as r
import datetime
import os

TOG =datetime.date.today() 
Date=datetime.date.today() + datetime.timedelta(days=1);

F=open("StudentsNameList.txt","r");
Names=F.readlines();
F.close();

Students_Name=[];
Students_RollNo=[];
Seat_Nos=[0];

for i in range(len(Names)):
	S=Names[i].split('\n');
	T=S[0].split('\t')
	Students_Name.append(T[0]);
	Students_RollNo.append(T[1]);

No_of_Students=len(Students_Name);
S_No=np.arange(1,No_of_Students+1);


while(len(Seat_Nos)<len(S_No)+1):
	Temp=r.randint(1,len(S_No));
	if(Temp not in Seat_Nos):
		Seat_Nos.append(Temp);

Seat_Nos.remove(0);

#os.system("del Seat_Allotment.doc");

F=open("Seat_Allotment.doc","w");

F.write("*Automatically Generated on "+str(TOG)+" @ IIIT-H using python");
F.write("\n\t\t\tComputer Problem Solving");
F.write("\n\t\t\t         CSE 602        ");
F.write("\n\t\t\t      Seat Allotment    ");
F.write("\n\t\t\t      ("+str(Date)+")");

F.write("\n");
F.write("---------------------------------------------------------");
F.write("\nS.No.\tSeat No\tRoll.No.\tName\n");
F.write("---------------------------------------------------------");
for i in range(len(S_No)):
	F.write("\n"+str(S_No[i])+"\t"+str(Seat_Nos[i])+"\t\t"+str(Students_Name[i])+"\t"+str(Students_RollNo[i]));

F.close();

F=open("Attendance.doc","w");

F.write("*Automatically Generated on "+str(TOG)+" @ IIIT-H using python");
F.write("\n*\'O\' marked are present\t\t*No. of Absentees : ");
F.write("\n\t\t\tComputer Problem Solving");
F.write("\n\t\t\t         CSE 602        ");
F.write("\n\t\t\t      Attendance Sheet");
F.write("\n\t\t\t      ("+str(Date)+")");

F.write("\n");
F.write("---------------------------------------------------------");
F.write("\nS.No.\tSeat No\tRoll.No.\tName\n");
F.write("---------------------------------------------------------");
for i in range(len(S_No)):
	F.write("\n"+str(S_No[i])+"\t"+str(Seat_Nos[i])+"\t\t"+str(Students_Name[i])+"\t"+str(Students_RollNo[i]));

F.close();

print":)Done ! "