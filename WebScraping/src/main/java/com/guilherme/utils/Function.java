package com.guilherme.utils;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.URL;
import java.util.List;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;
import org.apache.commons.io.FileUtils;

public class Function {
    public static void downloadFile(List<String> urlsPdf){
        try (ZipOutputStream zipOut = new ZipOutputStream(new FileOutputStream("Anexos.zip"))){
            for (int i = 0; i < urlsPdf.size(); i++) {
                URL url = new URL(urlsPdf.get(i));
                File file = new File("Anexo" + (i + 1) + ".pdf");
                FileUtils.copyURLToFile(url, file);
                zipFile(file, zipOut);
            }

            System.out.println("Processo concluído com êxito!");

        } catch (Exception e){
            throw new RuntimeException("Erro ao converter arquivos para pdf", e);
        }
    }

    public static void zipFile(File file, ZipOutputStream zipOut){
        try {
            zipOut.putNextEntry(new ZipEntry(file.getName()));
            FileUtils.copyFile(file, zipOut);
            file.deleteOnExit();
            zipOut.closeEntry();

        } catch (IOException io){
            throw new RuntimeException("Erro ao compactar diretório", io);
        }
    }

}
