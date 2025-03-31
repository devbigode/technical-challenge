package com.guilherme;

import com.guilherme.utils.Function;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;
import java.util.List;
import java.io.IOException;

public class Scraper {
    public static void main(String[] args) {
        try{
            /* Acesso a url e obtenção do conteúdo HTML da página */
            Document doc = Jsoup.connect("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos").get();

            /* Seleção específica dos "li items" onde estão os links dos pdfs */
            Elements elementLi = doc.select("div.cover-richtext-tile.tile-content").select("ol").select("li");

            /* Filtragem dos links de tipo .pdf e conversão para uma lista */
            List<String> urlsPdf = elementLi.select("a")
                    .eachAttr("href")
                    .stream()
                    .filter(url -> url.endsWith(".pdf"))
                    .toList();

            if (urlsPdf.size() != 2) {
                throw new RuntimeException("Falha ao encontrar os anexos");
            }

            /* Função responsável por converter URL em File e alocá-la em ./Anexos */
            Function.downloadFile(urlsPdf);

        } catch (IOException e){
            throw new RuntimeException(e);
        }
    }

}
