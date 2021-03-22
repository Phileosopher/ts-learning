<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="https://www.w3.org/1999/XSL/Transform" version="1.0">
<xsl:template match="/">

<HTML>
<head>
   <title>VBA Course Schedule</title>

<style>

div {
margin: auto;
width: 75%;
text-align: center
}

table, th, td {
border: 1px solid black;
border-collapse: collapse;
}

table {
width: 100%;
}

th {
height: 50px;
background-color: #4CAF50;
color: white;
font-size: 20px;
vertical-align: bottom;
}

th, td {
padding: 15px;
text-align: left;
}


tr:nth-child(even){
background-color: yellow;
}

p {
font-size: 12px;
font-face: Tahoma;
text-align: center;
}

</style>

</head>
<body>
<div>
<h2>VBA Course Schedule</h2>
<br/>
<table>
 <tr>
 	<th>Course Id</th>
	<th>Course Title</th>
	<th>Start Date</th>
	<th>No of Sessions</th>
 </tr>
<xsl:for-each select="Courses/Course">
 <tr>
	<td><xsl:value-of select="@ID" /></td>
	<td><xsl:value-of select="Title" /></td>
	<td><xsl:value-of select="Startdate" /></td>
	<td><xsl:value-of select="Sessions" /></td>
 </tr>
</xsl:for-each>
</table>
</div>
<h6>
<p>
Using Sample XSL Style Sheet 'Courses.xsl' prepared by Julitta Korol
</p></h6>
</body>
</HTML>
</xsl:template>
</xsl:stylesheet>  

