document.addEventListener("DOMContentLoaded", function(){
// make it as accordion for smaller screens
if (window.innerWidth > 992) {

	document.querySelectorAll('.navbar .nav-item').forEach(function(everyitem){

		everyitem.addEventListener('mouseover', function(e){

			let el_link = this.querySelector('a[data-bs-toggle]');

			if(el_link != null){
				let nextEl = el_link.nextElementSibling;
				el_link.classList.add('show');
				nextEl.classList.add('show');
			}

		});
		everyitem.addEventListener('mouseleave', function(e){
			let el_link = this.querySelector('a[data-bs-toggle]');

			if(el_link != null){
				let nextEl = el_link.nextElementSibling;
				el_link.classList.remove('show');
				nextEl.classList.remove('show');
			}

		})
	});

}
// end if innerWidth
}); 
//---------------
$('#myTab a').on('click', function (event) {
  event.preventDefault()
  $('#myTab').find('.active').removeClass('active');
  $(this).tab('show')
})
//------------
$('.dtlOfdots .clickDtlOftable').click(function(e){
	e.stopPropagation();
	$('.dtlOfdots .sideDotsDtl').hide();
	$(this).next('.sideDotsDtl').toggle();
})
$('body').click(function(e){
	e.stopPropagation();
	$('.dtlOfdots .sideDotsDtl').hide();
})
//-----linkedin Url - lead range-------
class Slider {
  constructor (rangeElement, valueElement, options) {
    this.rangeElement = rangeElement
    this.valueElement = valueElement
    this.options = options

    // Attach a listener to "change" event
    this.rangeElement.addEventListener('input', this.updateSlider.bind(this))
  }

  // Initialize the slider
  init() {
    this.rangeElement.setAttribute('min', options.min)
    this.rangeElement.setAttribute('max', options.max)
    this.rangeElement.value = options.cur

    this.updateSlider()
  }

  // Format the money
  asMoney(value) {
    return parseFloat(value)
      .toLocaleString('en-US', { maximumFractionDigits: 2 })
  }

  generateBackground(rangeElement) {   
    if (this.rangeElement.value === this.options.min) {
      return
    }

    let percentage =  (this.rangeElement.value - this.options.min) / (this.options.max - this.options.min) * 100
    return 'background: linear-gradient(to right, #ffbe0f, #ffbe0f ' + percentage + '%,  ' + percentage + '%, #dee1e2 100%)'
    // return 'background: linear-gradient(to right, #50299c, #7a00ff ' + percentage + '%, #d3edff ' + percentage + '%, #dee1e2 100%)'
  }

  updateSlider (newValue) {
    this.valueElement.innerHTML = this.asMoney(this.rangeElement.value)
    this.rangeElement.style = this.generateBackground(this.rangeElement.value)
  }
}

let rangeElement = document.querySelector('.range [type="range"]')
let valueElement = document.querySelector('.range .range__value span') 

let options = {
  min: 500,
  max: 10000,
  cur: 2500
}

if (rangeElement) {
  let slider = new Slider(rangeElement, valueElement, options)

  slider.init()
}
//---------------------------
$(document).on('input', '.inerRange', function() {
    $(this).next('.slider_value').html( $(this).val() );
});
//----------------
$('.eyeBox').click(function(){
  $(this).toggleClass('showEye');
})
//------------------
function viewfunction() {
  var temp = document.getElementById("tokenid");
  if (temp.type === "text") {
    temp.type = "password";
  }
  else {
    temp.type = "text";
  }
}

function viewfunction1() {
  var temp = document.getElementById("linkedinpass");
  if (temp.type === "text") {
    temp.type = "password";
  }
  else {
    temp.type = "text";
  }
}



