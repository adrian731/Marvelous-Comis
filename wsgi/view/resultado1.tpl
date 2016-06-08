%include('header.tpl')
		<table>
		%for x,y,z in zip(image,url,idcomic):
			<tr>
			<td>{{<img src="{{x}}.jpg"/></td>
			<td>{{y}}</td>
			<td>{{z}}</td>
			<tr>
		%end
		</table>
%include('footer.tpl')
