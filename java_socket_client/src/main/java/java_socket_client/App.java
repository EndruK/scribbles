package java_socket_client;

import java.io.IOException;
import java.net.UnknownHostException;

public class App {
    public static void main(String[] args) {
        SocketConnection conn = new SocketConnection();
        try {
            conn.startConnection("127.0.0.1", 8100);
            String text = "/**\n" +
                    " * Computational Intelligence Library (CIlib)\n" +
                    " * Copyright (C) 2003 - 2010\n" +
                    " * Computational Intelligence Research Group (CIRG@UP)\n" +
                    " * Department of Computer Science\n" +
                    " * University of Pretoria\n" +
                    " * South Africa\n" +
                    " *\n" +
                    " * This library is free software; you can redistribute it and/or modify\n" +
                    " * it under the terms of the GNU Lesser General Public License as published by\n" +
                    " * the Free Software Foundation; either version 3 of the License, or\n" +
                    " * (at your option) any later version.\n" +
                    " *\n" +
                    " * This library is distributed in the hope that it will be useful,\n" +
                    " * but WITHOUT ANY WARRANTY; without even the implied warranty of\n" +
                    " * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n" +
                    " * GNU Lesser General Public License for more details.\n" +
                    " *\n" +
                    " * You should have received a copy of the GNU Lesser General Public License\n" +
                    " * along with this library; if not, see <http://www.gnu.org/licenses/>.\n" +
                    " */\n" +
                    "package net.sourceforge.cilib.entity.operators.crossover.real;\n" +
                    "\n" +
                    "import com.google.common.base.Preconditions;\n" +
                    "import java.util.Arrays;\n" +
                    "import java.util.List;\n" +
                    "import net.sourceforge.cilib.controlparameter.ControlParameter;\n" +
                    "import net.sourceforge.cilib.controlparameter.RandomControlParameter;\n" +
                    "import net.sourceforge.cilib.entity.Entity;\n" +
                    "import net.sourceforge.cilib.entity.operators.crossover.CrossoverStrategy;\n" +
                    "import net.sourceforge.cilib.math.random.UniformDistribution;\n" +
                    "import net.sourceforge.cilib.type.types.container.Vector;\n" +
                    "\n" +
                    "public class ArithmeticCrossoverStrategy implements CrossoverStrategy {\n" +
                    "    \n" +
                    "    private ControlParameter lambda;\n" +
                    "    \n" +
                    "    public ArithmeticCrossoverStrategy() {\n" +
                    "        this.lambda = new RandomControlParameter(new UniformDistribution());\n" +
                    "    }\n" +
                    "    \n" +
                    "    public ArithmeticCrossoverStrategy(ArithmeticCrossoverStrategy copy) {\n" +
                    "        this.lambda = copy.lambda.getClone();\n" +
                    "    }\n" +
                    "\n" +
                    "    @Override\n" +
                    "    public ArithmeticCrossoverStrategy getClone() {\n" +
                    "        return new ArithmeticCrossoverStrategy(this);\n" +
                    "    }\n" +
                    "\n" +
                    "    @Override\n" +
                    "    public <E extends Entity> List<E> crossover(List<E> parentCollection) {\n" +
                    "        Preconditions.checkArgument(parentCollection.size() == 2, \"ArithmeticCrossoverStrategy requires 2 parents.\");\n" +
                    "\n" +
                    "        E o1 = (E) parentCollection.get(0).getClone();\n" +
                    "        E o2 = (E) parentCollection.get(1).getClone();\n" +
                    "        \n" +
                    "        Vector o1Vec = (Vector) o1.getCandidateSolution();\n" +
                    "        Vector o2Vec = (Vector) o2.getCandidateSolution();\n" +
                    "        \n" +
                    "        double value = lambda.getParameter();\n" +
                    "\n" +
                    "        o1.setCandidateSolution(o1Vec.multiply(value).plus(o2Vec.multiply(1.0 - value)));\n" +
                    "        o2.setCandidateSolution(o2Vec.multiply(value).plus(o1Vec.multiply(1.0 - value)));\n" +
                    "\n" +
                    "        return Arrays.asList(o1, o2);\n" +
                    "    }\n" +
                    "\n" +
                    "    public ControlParameter getLambda() {\n" +
                    "        return lambda;\n" +
                    "    }\n" +
                    "\n" +
                    "    public void setLambda(ControlParameter lambda) {\n" +
                    "        this.lambda = lambda";
            String resp = conn.sendMessage(text);
            System.out.println(resp);
            conn.stopConnection();
        } catch (UnknownHostException u) {
            System.out.println(u);
        } catch (IOException e) {
            System.out.println(e);
        }
    }
}
