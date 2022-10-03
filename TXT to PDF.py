#!/usr/bin/env python
# coding: utf-8

# In[10]:


from fpdf import FPDF
pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=15)
f=open("text.txt","r")
for x in f:
    pdf.cell(200,10,txt=x,ln=1,align='C')
pdf.output("programme.pdf")


# In[2]:


pip install fpdf


# In[ ]:





# In[ ]:





# In[ ]:




