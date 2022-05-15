$(document).ready(function() {
    // Setup - add a text input to each footer cell
    $('#example tfoot th').each( function () {
        var title = $(this).text();
        $(this).html( '<input type="text" class="form-control" placeholder="'+title+'" />' );
    } );
 
    // DataTable
    var table = $('#example').DataTable({
		responsive: true,
		
		"ordering": false,
        "info":     false,
		"dom": 'rt<"botton"<"row m-0"<"col"l><"col"p>>><"clear">',
		
	
		
		"language": {
		"lengthMenu": "Exibir _MENU_",
		"zeroRecords": "Nenhum registro encontrado",
		"info": "Pagina _PAGE_ de _PAGES_",
		"infoEmpty": "Nenhum registro encontrado",
		"infoFiltered": "(filtered from _MAX_ total records)",
		"paginate": {
				"first":      "Primeiro",
				"last":       "Ultimo",
				"next":       "Proximo",
				"previous":   "Anterior"
			},
		},
		
		initComplete: function () {
            // Apply the search
            this.api().columns().every( function () {
                var that = this;
 
                $( 'input', this.footer() ).on( 'keyup change clear', function () {
                    if ( that.search() !== this.value ) {
                        that
                            .search( this.value )
                            .draw();
                    }
                } );
            } );
		}
		
        /*initComplete: function () {
            // Apply the search
            this.api().columns().every( function () {
                var that = this;
 
                $( 'input', this.footer() ).on( 'keyup change clear', function () {
                    if ( that.search() !== this.value ) {
                        that
                            .search( this.value )
                            .draw();
                    }
                } );
            } );
        }*/
		
    });
	$('#pesquisa').keyup(function(){
	  table.search($(this).val()).draw() ;
	});
	
	// Setup - add a text input to each footer cell
    $('#example2 tfoot th').each( function () {
        var title = $(this).text();
        $(this).html( '<input type="text" class="form-control f-11 p-2" placeholder="'+title+'" />' );
    } );
 
    // DataTable
    var table2 = $('#example2').DataTable({
		responsive: true,
		
		"ordering": false,
        "info":     false,
		"dom": 'rt<"botton"<"row m-0"<"col"l><"col"p>>><"clear">',
		
	
		
		"language": {
		"lengthMenu": "Exibir _MENU_",
		"zeroRecords": "Nenhum registro encontrado",
		"info": "Pagina _PAGE_ de _PAGES_",
		"infoEmpty": "Nenhum registro encontrado",
		"infoFiltered": "(filtered from _MAX_ total records)",
		"paginate": {
				"first":      "Primeiro",
				"last":       "Ultimo",
				"next":       "Proximo",
				"previous":   "Anterior"
			},
		},
		
		initComplete: function () {
            // Apply the search
            this.api().columns().every( function () {
                var that = this;
 
                $( 'input', this.footer() ).on( 'keyup change clear', function () {
                    if ( that.search() !== this.value ) {
                        that
                            .search( this.value )
                            .draw();
                    }
                } );
            } );
		}
		
        /*initComplete: function () {
            // Apply the search
            this.api().columns().every( function () {
                var that = this;
 
                $( 'input', this.footer() ).on( 'keyup change clear', function () {
                    if ( that.search() !== this.value ) {
                        that
                            .search( this.value )
                            .draw();
                    }
                } );
            } );
        }*/
		
    });
	$('#pesquisa2').keyup(function(){
	  table2.search($(this).val()).draw() ;
	});
	
	
	
	
});




