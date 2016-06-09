%include('header.tpl')
<body background="/static/images/resultado2.jpg">
		<table>
		%for x,y in zip(img,idcomic):
			<tr>
			<td><a href="http://marvel.com/comics/issue/{{y}}/a"><img src="{{x}}"/></a></td>
			<td>
			<tr>
		%end
		</table>
%include('footer.tpl')
