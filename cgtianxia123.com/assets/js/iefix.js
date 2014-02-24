/**
 * @author
 */

$(document).ready(function() {
	if ($.browser.msie && parseInt($.browser.version, 10) <= 7) {

		$("#masthead").remove();
		$("#socialtab").remove();
		$("#tabie").show();
		$("#carouselselector").remove();
		$(".carousel").removeClass("main");
		$(".carousel").addClass("ie7hack");
		$("#tabselector").remove();
		$("#ietabs").show();
		$("#ie7alert").show();
		$("#ie7header").show();
		$("#ie7spacer").show();
		$("#exploreline").remove();
		$(".pagemode").css("margin-top", function(index) {
			return index - 0;
		});

	} else {
		$("#ie7alert").remove();
		$("#ie7header").remove();
		$("#masthead").show();
		$("#carouselselector").show();

	};
});