using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;

class CodeWriter {

    void Main() {

        MethodWriter();

    }

    void MethodWriter() {

        List<string> codeLines = new List<string>();

        using (var input = new StreamReader("path/to/file/the-file")) {

            while (!input.EndOfStream) codeLines.Add(input.ReadLine());

        }

        Console.WriteLine("Type: ");
        string type = Console.ReadLine();
        Console.WriteLine("Name: ");
        string name = Console.ReadLine();
        Console.WriteLine("Parameters: ");
        string parameters = Console.ReadLine();

        string method = $"        static {type} {name}({parameters})" + " {";

        codeLines.Insert(codeLines.Count - 4, "");
        codeLines.Insert(codeLines.Count - 4, method);
        codeLines.Insert(codeLines.Count - 4, "             ");
        codeLines.Insert(codeLines.Count - 4, "             ");
        codeLines.Insert(codeLines.Count - 4, "             ");
        codeLines.Insert(codeLines.Count - 4, "        }");

        using (var output = new StreamWriter("path/to/file/the-file")) {

            foreach (var line in codeLines) output.WriteLine(line);

        }

    }

}