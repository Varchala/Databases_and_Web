<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html>
    <body>
    <form>
   <xsl:apply-templates/>
    </form>
    </body>
    </html>
  </xsl:template>
 <xsl:template match="title">

  <h2><xsl:value-of select="caption"/></h2>

  </xsl:template>
  <xsl:template match="submit">
    <input type="submit">
      <xsl:attribute name="value">
        <xsl:value-of select="caption"/>
      </xsl:attribute>
      </input>
  </xsl:template>

   <xsl:template match="reset">
   <input type="reset">
      <xsl:attribute name="value">
        <xsl:value-of select="caption"/>
      </xsl:attribute>
      </input>
  </xsl:template>

  <xsl:template match="textbox">
    <label>
    <xsl:value-of  select="caption/text()"/>
    </label>
    
    <input type="text" >
     <xsl:attribute name="name">
        <xsl:value-of select="name"/>
      </xsl:attribute>
      <xsl:attribute name="size">
        <xsl:value-of select="size"/>
      </xsl:attribute>
      <xsl:attribute name="maxlength">
        <xsl:value-of select="maxlength"/>
      </xsl:attribute>
      
    </input>
  </xsl:template>

  <xsl:template match="checkboxes">
   <label>
    <xsl:value-of  select="caption/text()"/>
    </label>
    
        <xsl:variable name="cname">
    <xsl:value-of  select="name"/>
    </xsl:variable>
    <xsl:for-each select="checkboxgroup/checkbox">
      <label>
    <xsl:value-of  select="caption/text()"/>
    </label>
    <input type="checkbox" >
     <xsl:attribute name="value">
        <xsl:value-of select="value"/>
      </xsl:attribute>
      <xsl:attribute name="name">
        <xsl:copy-of select="$cname"/>
      </xsl:attribute>
        <xsl:choose>
         <xsl:when test="@status = 'checked'">
           <xsl:attribute name="checked">
        true
      </xsl:attribute>
         </xsl:when>
       </xsl:choose>
    </input>
    </xsl:for-each>
  </xsl:template>

  <xsl:template match="radio">

    <label>
    <xsl:value-of  select="caption/text()"/>
    </label>
    <xsl:variable name="rname">
    <xsl:value-of  select="name"/>
    </xsl:variable>
    <xsl:for-each select="radiogroup/radioelement">
    <label>
    <xsl:value-of  select="caption/text()"/>
    </label>
    <input type="radio" >
     <xsl:attribute name="value">
        <xsl:value-of select="value"/>
      </xsl:attribute>
      <xsl:attribute name="name">
        <xsl:copy-of select="$rname" />
      </xsl:attribute>
    </input>
    </xsl:for-each>

  </xsl:template>


  <xsl:template match="select">
   <label>
    <xsl:value-of  select="caption/text()"/>
    </label>
    <xsl:variable name="sname">
    <xsl:value-of  select="name"/>
    </xsl:variable>
    <select>
     <xsl:attribute name="name">
        <xsl:value-of select="name/text()"/>
      </xsl:attribute>
    
    <xsl:for-each select="options/option">
    
    <option>
     <xsl:attribute name="value">
        <xsl:value-of select="value"/>
      </xsl:attribute>
      <xsl:attribute name="name">
        <xsl:copy-of select="$sname" />
      </xsl:attribute>
      <xsl:value-of select="caption/text()"/>
    </option>
    </xsl:for-each>
    </select>
  </xsl:template>

  <xsl:template match="multiselect">
  <label>
    <xsl:value-of  select="caption/text()"/>
    </label>
    <xsl:variable name="mname">
    <xsl:value-of  select="name"/>
    </xsl:variable>
    <select multiple="true">
     <xsl:attribute name="name">
        <xsl:value-of select="name/text()"/>
      </xsl:attribute>
    <xsl:for-each select="options/option">
    
    <option>
     <xsl:attribute name="value">
        <xsl:value-of select="value"/>
      </xsl:attribute>
      <xsl:attribute name="name">
      <xsl:copy-of select="$mname" />
       </xsl:attribute>
      <xsl:value-of select="caption/text()"/>
    </option>
    </xsl:for-each>
    </select>
  </xsl:template>

  <xsl:template match="break">
  <br></br>
  </xsl:template>
</xsl:stylesheet>