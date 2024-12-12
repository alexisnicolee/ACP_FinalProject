
# *EvacuAid - Disaster Evacuation Management System*

**I. Project Overview**

In times of natural disasters, effective management and tracking of evacuees are crucial to ensure the safety and well-being of individuals and families. However, evacuation authorities often face significant challenges in collecting and organizing necessary information, especially when relying on manual methods such as paper and pen. These traditional methods are not only time-consuming but also inefficient, prone to human error, and lead to confusion, complicating the process of identifying which families have evacuated and managing large numbers of evacuees. **EvacuAid** is a Disaster Evacuation Management System designed to address the need for efficient and accurate tracking of evacuees during natural disasters. The main goal of the EvacuAid system is to offer a faster and more accurate way to track evacuees. The system ensures that all evacuees are accounted for, shelters are used effectively, and emergency responses are well-coordinated. By allowing families to register when they arrive at a shelter, the system reduces confusion and ensures that no family is left behind. The system supports the mission by improving disaster response and resource management, ultimately saving lives and reducing the impact of disasters. Included features of the system are family registration, real-time tracking of registered families, and capacity allocation for shelters. The target users include families who have evacuated, municipal disaster response teams, and local government authorities. 

**II. Python Concepts and Libraries**

*Python Tkinter*

In the EvacuAid system, the Tkinter library is employed to create a graphical user interface (GUI) that makes interacting with the system easier for users such as evacuees, authorities, and disaster response teams. Tkinter allows the design of windows, forms, and other components used by the users. Different interactive elements and functionalities are used to ensure that data is gathered, displayed, and updated in real-time. Tkinter's widgets are utilized to build input forms, buttons, labels, and other interactive elements that help users provide and view essential data. Entry widgets capture input from users when registering families, such as names, contact details, and addresses. Additionally, Tkinter is responsible for displaying the information entered, along with the status of the evacuation, real-time tracking data, and available shelter resources, allowing authorities to make quick, informed decisions. 

*MySQL*

For storing and managing the data gathered from families in the evacuation centers, the MySQL database system is used. MySQL is a relational database management system (RDBMS) that helps organize and store large amounts of structured data efficiently. It holds essential information about the evacuees, including family details, shelter assignments, and evacuation statuses. By using MySQL, the EvacuAid system can ensure that data is securely stored, easily queried, and updated in real-time. The system interacts with the MySQL database to store new entries when families register, update existing records as the evacuation status changes, and retrieve information quickly when authorities need to allocate resources or verify evacuation details. MySQL’s ability to handle large datasets with speed and reliability makes it an ideal choice for a disaster management system like EvacuAid. 

**III. Sustainable Development Goals**

The EvacuAid aligns with several Sustainable Development Goals (SDGs), particularly in areas related to disaster management, community resilience, and ensuring the safety and well-being of people. 

* **SDG 11: Sustainable Cities and Communities** – Disaster response and evacuation efficiency are crucial to reduce the impact of disasters on communities. EvacuAid ensures accurate registration and tracking of evacuees, protecting them during emergencies.  

* **SDG 3: Good Health and Well-being** – EvacuAid helps authorities quickly identify those needing immediate assistance during disasters, such as medical care and temporary shelter, reducing health risks and ensuring support throughout the crisis. 

* **SDG 16: Peace, Justice, and Strong Institutions** – EvacuAid promotes transparency and accountability, helping authorities make informed decisions with real-time data, ensuring fair and equitable resource distribution during crises, and building trust between the public and authorities. 

* **SDG 13: Climate Action** – EvacuAid enhances community resilience and preparedness for climate-related disasters by enabling faster and more organized responses.

**IV. Instructions**

* **Welcome Page** displays the welcome page for users. It starts with a greeting and shows the system's title, EvacuAid. The purpose of the system is also explained, helping users understand its function. Additionally, there is a "Proceed" button that, when clicked, takes users to the next page.

* **Registration Page** shows the family registration page for users. This page explains what information needs to be provided for tracking during evacuation. 

* **Verification Page** shows the page where users can verify the information they have provided. This page displays the exact details they entered, such as family information, contact information, and address details. There is also a "Back" button, allowing users to correct any mistakes in their information, and a "Next" button to proceed if the information is correct and has been verified.

* **Terms of Agreememt Page** shows the agreement that users need to read in order to understand that the information they provided will be used solely for evacuation purposes. This page allows users to confirm whether they agree to the terms and conditions of the system. There is also a "Back" button if they wish to return to the verification page, and an "I Agree" button if they agree with the terms outlined in the system.

* **Successfully Registered Page** shows that the user has been successfully registered in the system, meaning they are now listed as evacuees at the evacuation center. Additionally, there is a "View Data" button that will take them to the final page of the system

* **Data Page** the second to the page of the system, which displays the overall data of those who have registered. It shows a list of all evacuees along with the information they provided.  There is also a 'View Total Individual' button, which allows you to see the total number of people currently inside the evacuation center when clicked. Finally, there is an "Exit" button that allows users to leave the system, signaling that they have finished using it.

* **Evacuation Report Page** this is the last page, which displays the report containing the total number of individuals currently in the evacuation center, as well as the overall count of families present. In addition to this, there is a back button provided that allows you to easily navigate back to the data table page, where you can view or update the detailed information.

