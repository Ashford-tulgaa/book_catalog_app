{{/*
==================================================
Helm Helper Functions
==================================================
These helper templates avoid repeating names
throughout the chart.
*/}}

{{/*
Returns the application name.
Used for labels and selectors.
*/}}
{{- define "book-catalog-api.name" -}}
book-catalog-api
{{- end }}

{{/*
Returns the full resource name.
Used when naming Deployments, Services,
ConfigMaps and Secrets.
*/}}
{{- define "book-catalog-api.fullname" -}}
{{ include "book-catalog-api.name" . }}
{{- end }}