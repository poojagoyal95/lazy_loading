$(document).ready(function () {
    $(window).on('scroll', function() {
		var next = $('#lazyLoadLink').attr('data-next');
		if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight && next == 1) {
			var page = $('#lazyLoadLink').attr('data-page');
			console.log(page)
			$.ajax({
				type: 'post',
				url: '/lazy_load_posts/',
				data: {
					'page': page,
					'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value
				},
				success: function(data) {
					console.log(data)
					
					// append html to the posts div
					$('#appenddata').append(data.posts_html);
					$("#lazyLoadLink").attr("data-next", data.has_next)
					$("#lazyLoadLink").attr("data-page", data.page_number)
				},
				error: function(xhr, status, error) {
					// shit happens friends!
					console.log(error)
				}
			});
		}
    }) 
});
