var Autocomplete = function(options) {
      
    // Multiple selelectors to make this reusable 
    this.form_selector = options.form_selector
    this.input_selector = options.input_selector
    this.container_selector = options.container_selector

    this.url = options.url || AUTOCOMPLETE_URL_RESOURCEBASE
    this.delay = parseInt(options.delay || 300)
    this.minimum_length = parseInt(options.minimum_length || 1)
    this.form_elem = null
    this.query_box = null
  }

  Autocomplete.prototype.setup = function() {
    var self = this

    this.form_elem = $(this.form_selector);
    this.query_box = this.form_elem.find($(this.input_selector));
    this.query_container = this.form_elem.find($(this.container_selector));

    // Watch the input box.
    this.query_box.on('keyup', function() {
  
      var query = self.query_box.val()

      if(query.length < self.minimum_length) {
        $('.ac-results').remove() // Remove autocomplete when no input
        return false
      }
    
      self.fetch(query)
    })

    // On selecting a result, populate the search field.
    this.form_elem.on('click', '.ac-result', function(ev) {
      self.query_box.val($(this).text())
      $('.ac-results').remove()
      return false
    })
  }

  Autocomplete.prototype.fetch = function(query) {
    var self = this

    $.ajax({
      url: this.url
    , data: {
        'q': query
      }
    , success: function(data) {
        self.show_results(data)
      }
    })
  }

  Autocomplete.prototype.show_results = function(data) {
    // Remove any existing results.
    $('.ac-results').remove()

    // Mapping to the item text and limiting results shown to 10 only rather
    // than scrolling.
    var results = data.results.map(item => item.text).slice(0, 10) || []
    var results_wrapper = $('<div class="ac-results"></div>')
    var base_elem = $('<div class="result-wrapper"><a href="#" class="ac-result"></a></div>')


    if(results.length > 0) {
      for(var res_offset in results) {
        var elem = base_elem.clone()
        // Don't use .html(...) here, as you open yourself to XSS.
        // Really, you should use some form of templating.
        elem.find('.ac-result').text(results[res_offset])
        results_wrapper.append(elem)
      }
    }
    else {
      var elem = base_elem.clone()
      elem.text("No results found.")
      results_wrapper.append(elem)
    }

    this.query_box.after(results_wrapper)
  }
