SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode
    # or set False to use SummernoteInplaceWidget - no iframe mode
    'iframe': False,

    'width': '100%',
    'height': '240',
    'lang': 'ko-KR',

    # Customize toolbar buttons
    'toolbar': [
        ['style', ['style']],
        ['style', ['bold', 'italic', 'underline', 'clear']],
        ['para', ['ul', 'ol']],
        # ['insert', ['link', 'picture']],
        # ['view', ['fullscreen']],
    ],

    # Set external media files for SummernoteInplaceWidget.
    # !!! Be sure to put {{ form.media }} in template before initiate summernote.
    'inplacewidget_external_css': (),
    'inplacewidget_external_js': ()
}
