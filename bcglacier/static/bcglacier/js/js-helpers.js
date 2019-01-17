
function setPark(park)
{
  // alert("before setting vars");
  //print request.session.get('current_park_name')

  $.post('update_park/', {park: park});
};

function rate(num)
{
    document.getElementById("stars").value = num;
	if (num >= 1)	{
		document.getElementById("star1").src="/static/bcglacier/images/star-filled.png";
	}
	else {
		document.getElementById("star1").src="/static/bcglacier/images/star-empty.png";
	}

	if (num >= 2)	{
		document.getElementById("star2").src="/static/bcglacier/images/star-filled.png";
	}
	else {
		document.getElementById("star2").src="/static/bcglacier/images/star-empty.png";
	}

	if (num >= 3)	{
		document.getElementById("star3").src="/static/bcglacier/images/star-filled.png";
	}
	else {
		document.getElementById("star3").src="/static/bcglacier/images/star-empty.png";
	}

	if (num >= 4)	{
		document.getElementById("star4").src="/static/bcglacier/images/star-filled.png";
	}
	else {
		document.getElementById("star4").src="/static/bcglacier/images/star-empty.png";
	}

	if (num >= 5)	{
		document.getElementById("star5").src="/static/bcglacier/images/star-filled.png";
	}
	else {
		document.getElementById("star5").src="/static/bcglacier/images/star-empty.png";
	}

};
