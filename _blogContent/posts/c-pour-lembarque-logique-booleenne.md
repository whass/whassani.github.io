title: 'C pour l''embarqué : Logique Booléenne'
date: 2014-02-14
categories: 
- Embedded



<table > 
<tbody >
<tr >

<td colspan="2" rowspan="1" >







Lois fondamentale de bool






</td>
</tr>
<tr >

<td >







A& B = B & A






</td>

<td >







Loi commutative






</td>
</tr>
<tr >

<td >







A |B = B | A






</td>

<td >







Loi commutative






</td>
</tr>
<tr >

<td >







(A & B) & C = A & (B & C)






</td>

<td >







Loi associative






</td>
</tr>
<tr >

<td >







(A | B) | C = A | (B | C)






</td>

<td >







Loi associative






</td>
</tr>
<tr >

<td >







(A | B) & C = (A & C) | (B & C)






</td>

<td >







Loi distributive






</td>
</tr>
<tr >

<td >







(A & B) | C = (A | C) & (B | C)






</td>

<td >







Loi distributive






</td>
</tr>
<tr >

<td >







A& 0 = 0






</td>

<td >







Identité de 0






</td>
</tr>
<tr >

<td >







A |0 = A






</td>

<td >







Identité de 0






</td>
</tr>
<tr >

<td >







A& 1 = A






</td>

<td >







Identité de 1






</td>
</tr>
<tr >

<td >







A |1 = 1






</td>

<td >







Identité de 1






</td>
</tr>
<tr >

<td >







A |A = A






</td>

<td >







Propriété de OU






</td>
</tr>
<tr >

<td >







A | (~A) = 1






</td>

<td >







Propriété de OU






</td>
</tr>
<tr >

<td >







A& A= A






</td>

<td >







Propriété de ET






</td>
</tr>
<tr >

<td >







A & (~A) = 0






</td>

<td >







Propriété de ET






</td>
</tr>
<tr >

<td >







~(~A) = A






</td>

<td >







Inverse






</td>
</tr>
<tr >

<td >







~(A | B) = (~A) & (~B)






</td>

<td >







Théorème De Morgan






</td>
</tr>
<tr >

<td >







~(A & B) = (~A) | (~B)






</td>

<td >







Théorème De Morgan






</td>
</tr>
</tbody>
</table>



