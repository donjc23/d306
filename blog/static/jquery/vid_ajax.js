var videos, $vid_links = $("#vid_list a"), $iframe = $("#vid iframe"), $caption = $("#caption");
	
	$.get("{{ STATIC_URL }}/json/videos.json", function(data){
			videos = data;
	})

	$vid_links.click(function(){
		var index = $vid_links.index(this);
		var video = videos[index].video;
		$caption.text(video.caption);
		$iframe.attr("src", video.source);
		return false;
	})