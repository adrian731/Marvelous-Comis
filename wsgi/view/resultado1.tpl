%include('header.tpl')
<body background="/static/images/resultado1.jpg">
		<table>
		%for x,y,z in zip(img,url,idcomic):
			<tr>
			<td><a href="http://marvel.com/comics/issue/{{z}}/a"><img src="{{x}}"/></a></td>
			<tr>
		%end
		</table>
%include('footer.tpl')
