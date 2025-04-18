#include <gtk/gtk.h>
#include <webkit2/webkit2.h>

static void load_url(GtkWidget *entry, WebKitWebView *web_view) {
    const char *url = gtk_entry_get_text(GTK_ENTRY(entry));
    if (url && url[0] != '\0') {
        char *formatted_url;
        if (g_str_has_prefix(url, "http://") || g_str_has_prefix(url, "https://")) {
            formatted_url = g_strdup(url);
        } else {
            formatted_url = g_strdup_printf("http://%s", url);
        }
        webkit_web_view_load_uri(web_view, formatted_url);
        g_free(formatted_url);
    }
}

int main(int argc, char *argv[]) {
    gtk_init(&argc, &argv);

    // Create main window
    GtkWidget *window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_default_size(GTK_WINDOW(window), 800, 600);
    gtk_window_set_title(GTK_WINDOW(window), "YOS Browser");

    // Create vertical layout
    GtkWidget *vbox = gtk_box_new(GTK_ORIENTATION_VERTICAL, 5);
    gtk_container_add(GTK_CONTAINER(window), vbox);

    // Create entry for URL input
    GtkWidget *entry = gtk_entry_new();
    gtk_box_pack_start(GTK_BOX(vbox), entry, FALSE, FALSE, 0);

    // Create WebView for displaying web pages
    WebKitWebView *web_view = WEBKIT_WEB_VIEW(webkit_web_view_new());
    gtk_box_pack_start(GTK_BOX(vbox), GTK_WIDGET(web_view), TRUE, TRUE, 0);

    // Connect signal to load URL when Enter is pressed
    g_signal_connect(entry, "activate", G_CALLBACK(load_url), web_view);

    // Handle window close
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

    gtk_widget_show_all(window);
    gtk_main();

    return 0;
}
