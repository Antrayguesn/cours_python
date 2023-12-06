export PLANTUML_URL="https://uml.aigyre.fr/"
bundle exec asciidoctor-revealjs -r asciidoctor-plantuml Presentation/presentation.adoc -o build/presentation.html
bundle exec asciidoctor -r asciidoctor-plantuml Presentation/presentation.adoc -o build/cours.html
bundle exec asciidoctor -r asciidoctor-plantuml TP/LaMissionDeCesar.adoc -o build/TP.html

docker build . -t registry.aigyre.fr/tp:latest

docker push registry.aigyre.fr/tp:latest
