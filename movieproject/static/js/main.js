/*---------Functionality like Pagination, filter--------------*/
$(document).ready(function(){
	/*---------Html of movie list------------*/
	function MovieListHtml(movies){
		var str='';
		$.each(movies, function(i, val){
			str+='<tr><td>'+val['title']+'</td>';
			str+='<td>'+val['description']+'</td>';
			str+='<td><image class="featured_img" src="'+val['featured_image']+'"/"></td>';
			str+='<td>'+val['languages']+'</td>';
			str+='<td>'+val['genres']+'</td>';
			str+='<td>'+val['movie_length']+'</td>';
			str+='<td>'+val['resease_date']+'</td></tr>';
		});
		if(str == ''){
			str='<tr><td colspan="7">No Record Found.</td></tr>';
		}	
		return str;
	}
	/*-----------Function for making pagination index----------*/
	function MakeIndex(count, page_id){
		var str='<li><b>Pages: </b></li>';
		var p = Math.floor((count-1)/10)+1;
		if(p == 0){
			p=1;
		}
		for (var i = 1; i <= p; i++) {
			if(i == page_id){
				str+='<li class="active pointer page">'+i+'</li>';
			}
			else{
				str+='<li class="pointer page">'+i+'</li>';
			}
			if(i != p){
				str+='<li > | </li>';
			}
		};
		$('#index').html(str);
	}
	/*----------Ajax call for loading page------------*/	
	var load_page=function(page_id){
		$.ajax({url:'/loadpage/',
				type:'GET',
				dataType:'JSON',
				data:$('#criteria_form').serialize()+'&page_id='+page_id,
				success:function(res){
					if(res['result'] == 'SUCCESS'){
						$('#movie_table tbody').html(MovieListHtml(res['movies']));
						MakeIndex(res['total_count'], page_id);
					}	
				},
			});
	};
	/*--------Change event on filters select-----------*/
	$('#id_genre, #id_language').change(function(){
		load_page(1);
	});
	/*--------Change event on sort by select-----------*/
	$('#id_sort_by').change(function(){
		
		load_page(parseInt($('#index li.active').text()));
	});
	/*--------Click event on pagination section-----------*/
	$('#index').on('click','li.page',function(){
		load_page(parseInt($(this).text()));
	});
	/*-------- Initialize Page-----------*/
	load_page(1);

});	