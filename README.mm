<map version="freeplane 1.7.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="Freeplane Tools" FOLDED="false" ID="ID_1002858447" CREATED="1629749144699" MODIFIED="1629938895387" STYLE="oval">
<font SIZE="18"/>
<hook NAME="MapStyle">
    <properties edgeColorConfiguration="#808080ff,#ff0000ff,#0000ffff,#00ff00ff,#ff00ffff,#00ffffff,#7c0000ff,#00007cff,#007c00ff,#7c007cff,#007c7cff,#7c7c00ff" show_icon_for_attributes="true" show_note_icons="true" fit_to_viewport="false"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" ICON_SIZE="12.0 pt" COLOR="#000000" STYLE="fork">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval" SHAPE_HORIZONTAL_MARGIN="10.0 pt" SHAPE_VERTICAL_MARGIN="10.0 pt">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,5"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,6"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,7"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,8"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,9"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,10"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,11"/>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="15" RULE="ON_BRANCH_CREATION"/>
<hook NAME="accessories/plugins/AutomaticLayout.properties" VALUE="ALL"/>
<richcontent TYPE="NOTE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      If you hate writing Markdown, but love mindmaps (and using [freeplane](https://www.freeplane.org/wiki/index.php/Home) this toolset is for you.
    </p>
    <p>
      
    </p>
    <p>
      These python programs aim to ease translating a mindmap into various markdown formats.
    </p>
    <p>
      
    </p>
    <p>
      This document [README.md](./README.md) was made with `mm2github.py` with &#160;[README.mm](./README.mm) as a source.
    </p>
    <p>
      
    </p>
    <p>
      Enjoy!
    </p>
    <p>
      
    </p>
    <p>
      Pull requests welcome. :)
    </p>
  </body>
</html>
</richcontent>
<node TEXT="Installation" POSITION="right" ID="ID_143871825" CREATED="1629902324496" MODIFIED="1631380965335">
<edge COLOR="#ff0000"/>
<richcontent TYPE="NOTE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      To install this package from [pypy](https://pypi.org/project/ps1/) run the following command.
    </p>
    <p>
      
    </p>
    <p>
      ```
    </p>
    <p>
      pip3 install ps1
    </p>
    <p>
      ```
    </p>
  </body>
</html>

</richcontent>
</node>
<node TEXT="License" POSITION="right" ID="ID_1578673671" CREATED="1629902379529" MODIFIED="1629902575114">
<edge COLOR="#00ff00"/>
<richcontent TYPE="NOTE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      See: [LICENSE](./LICENSE)
    </p>
  </body>
</html>
</richcontent>
</node>
<node TEXT="Quickstart" POSITION="right" ID="ID_254775212" CREATED="1629939067633" MODIFIED="1629939291687">
<edge COLOR="#ff0000"/>
<richcontent TYPE="NOTE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      Run the following if you want a quick demo of how this works. Have `freeplane` installed before running this.
    </p>
    <p>
      
    </p>
    <p>
      ```
    </p>
    <p>
      pip3 install freeplane_tools
    </p>
    <p>
      
    </p>
    <p>
      mm2template.py mymindmap.mm
    </p>
    <p>
      
    </p>
    <p>
      freeplane mymindmap.mm
    </p>
    <p>
      
    </p>
    <p>
      # do your editing in freeplane
    </p>
    <p>
      
    </p>
    <p>
      mm2github.py -w mymindmap.mm
    </p>
    <p>
      
    </p>
    <p>
      ```<br/>
    </p>
    <p>
      This will create: `mymindmap.md`
    </p>
  </body>
</html>
</richcontent>
<node TEXT="Example" ID="ID_1638091866" CREATED="1629938015115" MODIFIED="1629939356849"><richcontent TYPE="NOTE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      Just want to look?
    </p>
    <p>
      
    </p>
    <p>
      [This](./examples/template.mm) mindmap produces the following [markdown](./examples/template.md)
    </p>
  </body>
</html>
</richcontent>
</node>
</node>
<node TEXT="CLI Commands" POSITION="right" ID="ID_433247386" CREATED="1629929022711" MODIFIED="1629930535606">
<edge COLOR="#00ffff"/>
<richcontent TYPE="NOTE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      __CLI_COMMANDS__
    </p>
  </body>
</html>
</richcontent>
</node>
<node TEXT="Building" POSITION="right" ID="ID_272462447" CREATED="1629902345130" MODIFIED="1630074634111">
<edge COLOR="#0000ff"/>
<attribute NAME="child" VALUE="list"/>
<richcontent TYPE="NOTE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      os / Package prerequisites:
    </p>
    <p>
      ```
    </p>
    <p>
      pip3 install twine pydoctor
    </p>
    <p>
      ```
    </p>
  </body>
</html>
</richcontent>
<node TEXT="Install Locally from current branch" ID="ID_1204653861" CREATED="1629933386693" MODIFIED="1630076932495">
<node TEXT="```&#xa;make install_local&#xa;```" ID="ID_672893705" CREATED="1629933401816" MODIFIED="1629933419483"/>
</node>
<node TEXT="Build Package" ID="ID_65759878" CREATED="1629933421052" MODIFIED="1630074652959">
<node TEXT="```&#xa;make pkg&#xa;```" ID="ID_1653643308" CREATED="1629933431213" MODIFIED="1629933438239"/>
</node>
<node TEXT="Release" ID="ID_544074610" CREATED="1630074625527" MODIFIED="1630074640189">
<node TEXT="```make documentation```" ID="ID_939118802" CREATED="1630074658121" MODIFIED="1630074832640">
<node TEXT="Make sure git tree is clean" ID="ID_1717393270" CREATED="1630076700962" MODIFIED="1630076706964"/>
</node>
<node TEXT="```make bump_release```" ID="ID_1481426147" CREATED="1630074832858" MODIFIED="1630074842457"/>
<node TEXT="```make release```" ID="ID_1233882906" CREATED="1630074843085" MODIFIED="1630074853692"/>
</node>
</node>
<node TEXT="Other Docs" POSITION="right" ID="ID_1589081779" CREATED="1630019734423" MODIFIED="1630082904717">
<edge COLOR="#00ff00"/>
<richcontent TYPE="NOTE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      * [Api Docs](https://shollingsworth.github.io/freeplane_tools/)
    </p>
    <p>
      * [Changelog](./CHANGELOG.md)
    </p>
  </body>
</html>
</richcontent>
</node>
</node>
</map>
